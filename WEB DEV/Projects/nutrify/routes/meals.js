module.exports = (app) => {
    // Store meals
    let meals = []

    // Get all meals
    app.get('/meals', (req, res) => {
        return res.send(meals)
    })

    // Add new meal
    app.post('/meals', (req, res) => {
        let meal = req.body
        meal.id = Date.now()
        meals.push(meal)
        return res.send(meal)
    })

    // Delete meal
    app.delete('/meals/:id', (req, res) => {
        let id = parseInt(req.params.id)
        const index = meals.map(o => o.id).indexOf(id)
        if(index !== -1) {
            meals.splice(index, 1)
        }
        return res.send()
    })
}