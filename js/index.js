exports.leagueTable = async (req, res) => {
    const leagueTable =[
        {player: "Mum", points: 1, goals: 4},
        {player: "Suzi", points: 1, goals: 3},
        {player: "Random", points: 1, goals: 3},
        {player: "Iain", points: 1, goals: 3},
        {player: "Ste", points: 0, goals: 0}
    ]
    res.send({leagueTable})
}