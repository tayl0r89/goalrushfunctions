const Firestore = require('@google-cloud/firestore')
const PROJECTID = 'goalrush'
const FIXTURES = 'fixtures'
const db = new Firestore({
  projectId: PROJECTID
})

scrapeFixtures = async (req, res) => {
    const getText = async (element) => {
        return page.evaluate(element => element.textContent, element);
    }
    const batch = db.batch()
    const puppeteer = require('puppeteer-extra')
    const StealthPlugin = require('puppeteer-extra-plugin-stealth')
    puppeteer.use(StealthPlugin())
    const browser = await puppeteer.launch({args: ['--no-sandbox']});
    const page = await browser.newPage();
    await page.goto("https://www.footballpools.com/pool-games/goal-rush");
    const items = await page.$$('div.goal_rush_8')
    const fixtures = []
    for(let i=0; i < items.length; i++){
        const numberElement = await items[i].$('div.number')
        const homeElement = await items[i].$('div.home')
        const awayElement = await items[i].$('div.away')
        const number = numberElement ? await getText(numberElement) : undefined
        const home = homeElement ? await getText(homeElement) : undefined
        const away = awayElement ? await getText(awayElement) : undefined
        if(number != null && home != null && away != null){
            const newRef = db.collection(FIXTURES).doc()
            batch.set(newRef, {number, home, away})
        }
    }
    await batch.commit()
}

console.log("Scraping fixtures.")
scrapeFixtures().then(res => console.log("Complete"))