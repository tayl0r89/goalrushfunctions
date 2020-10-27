const Firestore = require('@google-cloud/firestore')
const PROJECTID = 'goalrush'
const FIXTURES = 'fixtures'
const db = new Firestore({
  projectId: PROJECTID
})

exports.fixtures = async (req, res) => {
  const results = await db.collection(FIXTURES).get()
  const fixtures = []
  results.forEach(d => {
    fixtures.push(d.data())
  })
  res.send({
    "fixtures": fixtures.sort((a,b) => a.number > b.number)
  })
}