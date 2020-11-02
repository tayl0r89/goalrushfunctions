const Firestore = require('@google-cloud/firestore')
const moment = require("moment")
const PROJECTID = 'goalrush'
const FIXTURES = 'fixtures'
const GAMEWEEK = 'gameweek'
const db = new Firestore({
  projectId: PROJECTID
})
const GAMEWEEK_DATE_FORMAT = "DD MMM @ HH:mm"

getLatestGameweek = async () => {
    const gameweekCollection = db.collection(GAMEWEEK)
    const gameweek = gameweekCollection.orderBy('date', 'desc').limit(1).get()
    return gameweek.exists ? gameweek.data() : null
}

getText = async (element) => {
    return element.evaluate(element => element.textContent, element);
}

getNumber = async (element) => {
    const value = await element.evaluate(element => element.textContent, element)
    return Number.parseInt(value)
}

getGameDate = async (element) => {
    const dateString = await element.evaluate(element => element.textContent, element)
    return moment(dateString, GAMEWEEK_DATE_FORMAT).toDate()
}

createGameWeek = async (date, id) => {
    const gameWeekCollection = db.collection(GAMEWEEK)
    const gameweek = {date, id}
    await gameWeekCollection.doc("" + id).set(gameweek)
    return gameweek
}

getGameWeek = async (gameweekDate, latestGameWeek) => {
    if(latestGameWeek != null){
        console.log("Found existing gameweek with id: " + latestGameWeek.id)
        if(latestGameWeek.date === gameweekDate){
            console.log("Lastest gameweek is the current one.")
            return latestGameWeek
        }
        return createGameWeek(gameweekDate, latestGameWeek.id + 1)
    }
    return createGameWeek(gameweekDate, 0)
}

scrapeFixtures = async (req, res) => {
    const puppeteer = require('puppeteer-extra')
    const StealthPlugin = require('puppeteer-extra-plugin-stealth')
    puppeteer.use(StealthPlugin())
    const browser = await puppeteer.launch({args: ['--no-sandbox']});
    const page = await browser.newPage();
    await page.goto("https://www.footballpools.com/pool-games/goal-rush");
    const dateElement = await page.$("p.closing-time span.date")
    const gameWeekDate = await getGameDate(dateElement)
    const latestGameWeek = await getLatestGameweek()
    const gameWeek = await getGameWeek(gameWeekDate, latestGameWeek)
    console.log(gameWeek)
    const batch = db.batch()
    const items = await page.$$('div.goal_rush_8')
    for(let i=0; i < items.length; i++){
        const numberElement = await items[i].$('div.number')
        const homeElement = await items[i].$('div.home')
        const awayElement = await items[i].$('div.away')
        const number = numberElement ? await getNumber(numberElement) : undefined
        const home = homeElement ? await getText(homeElement) : undefined
        const away = awayElement ? await getText(awayElement) : undefined
        if(number != null && home != null && away != null){
            const newRef = db.collection(FIXTURES).doc(home + away + gameWeek.id)
            batch.set(newRef, {number, home, away, gameWeekId: gameWeek.id})
        }
    }
    await batch.commit()
}

console.log("Scraping fixtures.")
scrapeFixtures().then(res => console.log("Complete"))