class Meal {
	constructor() {
		this.meals = []

		const form = document.querySelector('.meal-form')
		const title = document.querySelector('#title')
		const calories = document.querySelector('#calories')

		form.addEventListener('submit', (e) => {
			e.preventDefault()

			if(title.value !== '' && calories.value !== '') {
				this.addMeal({
					id: Date.now(),
					title: title.value,
					calories: calories.value
				})
			} else {
				this.showError('Please fill out both fields.', 'error')
			} 
		})
	}

	// AJAX request inside a promise
	request(method, url, data = null) {
		return new Promise((resolve, reject) => {
			let xhr = new XMLHttpRequest()
			xhr.open(method, url, true)
			xhr.setRequestHeader('Content-Type', 'application/json')
			xhr.onload = () => {
				if(xhr.status === 200) {
					return resolve(JSON.parse(xhr.responseText || '{}'))
				} else {
					return reject(new Error(`Request failed: ${xhr.status}`))
				}
			}

			if(data) {
				xhr.send(JSON.stringify(data))
			} else {
				xhr.send()
			}
		})
	}

	// Get meals
	async init() {
		try {
			this.meals = await this.request('GET', '/meals')
			this.render()
		} catch(error) {
			console.log(`Failed to get meals: ${error.message}`)
		}
	}
	
	// Add meal
	async addMeal(data) {
		try {
			const meal = await this.request('POST', '/meals', data)
			const list = document.querySelector('.meal-list')
			list.appendChild(this.createMeal(meal))
			this.meals.push(meal)
			this.updateTotalCalories()
		} catch(error) {
			console.log(`Failed to add meal: ${error.message}`)
		}
	}

	// Delete meal
	async deleteMeal(id) {
		try {
			await this.request('DELETE', `/meals/${id}`)
			let index = this.meals.map(meal => meal.id).indexOf(id)
			this.meals.splice(index, 1)
			this.updateTotalCalories()
		} catch(error) {
			console.log(`Failed to delete meal: ${error.message}`)
		}
	}

	// Calculate total calories
	updateTotalCalories() {
		let calories = this.meals.reduce((total, meal) => {
			return total + Number(meal.calories)
		}, 0)
		let totalCalories = document.querySelector('.total')
		totalCalories.innerHTML = calories.toLocaleString()
	}

	// Create meal
	createMeal({id, title, calories}) {
		let li = document.createElement('li')
		li.innerHTML = `
			<div class="meal-item">
				<p class="meal-title">${title}</p>
				<span class="meal-calories">${calories}</span>
				<a class="delete" href="#">&times;</a>
			</div>
		`

		// event listener - delete button
		li.querySelector('a').addEventListener('click', (e) => {
			e.preventDefault()
			this.deleteMeal(id)
			li.remove()
		})
		return li
	}

	// Show error
	showError(message, type) {
		const container = document.querySelector('.meals-container')
		const form = document.querySelector('.meals-container h2')
		const div = document.createElement('div')

		div.innerHTML = message
		div.classList.add(type)
		container.insertBefore(div, form)

		setTimeout(() => {
			div.remove()
		}, 4000)
	}

	// Render
	render() {
		let mealList = document.querySelector('.meal-list')
		let fragment = document.createDocumentFragment() 

		this.meals.forEach(meal => {
			fragment.appendChild(this.createMeal(meal))
		})

		mealList.appendChild(fragment)
		this.updateTotalCalories()
	}
}

let app = new Meal()
app.init()