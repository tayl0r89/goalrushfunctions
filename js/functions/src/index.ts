import * as functions from 'firebase-functions'
import * as firestore from '@google-cloud/firestore'

// // Start writing Firebase Functions
// // https://firebase.google.com/docs/functions/typescript
//
// export const helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });

const PROJECTID = 'goalrush'
const FIXTURE_SUMMARIES = 'fixtureSummaries'
const db = new firestore.Firestore({
  projectId: PROJECTID,
})

interface Fixture {
    home: string,
    away: string,
    number: number
}

interface Statistic {
    name: string,
    value: number
}

interface FixtureSummary {
    fixture: Fixture
    homeTeamBTTS: boolean[]
    awayTeamBTTS: boolean[]
    homeTeamHomeBTTS: boolean[]
    awayTeamAwayBTTS: boolean[]
    gameStats: Statistic[]
    bttsStats: Statistic[]
    gameRating: number
}

exports.fixtureSummaries = functions.https.onRequest(async (req, res) => {
  const results = await db.collection(FIXTURE_SUMMARIES).get()
  const summaries: FixtureSummary[] = []
  results.forEach(d => {
    summaries.push(d.data() as FixtureSummary)
  })
  res.send({
    summaries,
  })
})