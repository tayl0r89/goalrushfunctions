const Firestore = require('@google-cloud/firestore')
const PROJECTID = 'goalrush'
const COLLECTION_NAME = 'fixtures'
const db = new Firestore({
  projectId: PROJECTID
})

exports.fixtures = async (req, res) => {
  const home = "home"
  const away = "away"
  const number = 1
  const document = await db.collection(COLLECTION_NAME).add({ home, away, number })
  res.send({document})
}