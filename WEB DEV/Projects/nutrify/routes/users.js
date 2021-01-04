const express = require('express')
const router = express.Router()
const bcrypt = require('bcryptjs')


// User model
const User = require('../models/User')

// Login page
router.get('/login', (req, res) => res.render('login', {page: 'login'}))

// Register page
router.get('/register', (req, res) => res.render('register', {page: 'register'}))
// app.get('/register',(req, res) => {
//     res.status(200).render('register', { page: "register"})
//   });

// Register handle
router.post('/register', (req, res) => {
    const { name, email, password, password2 } = req.body
    
    let errors = []

    // Check required fields
    if(!name || !email || !password || !password2) {
        errors.push({ msg: 'Please fill in all fields.' })
    }

    // Check passwords match
    if(password !== password2) {
        errors.push({ msg: `Passwords don't match.` })
    }

    // Check password length
    if(password.length < 6) {
        errors.push({ msg: 'Password must be at least six characters.' })
    }

    // Check for errors
    if(errors.length > 0) {
        res.render('register', {
            page: 'register',
            errors,
            name,
            email,
            password,
            password2
        })
    } else {
        // Check if user exists
        User.findOne({ email: email })
            .then(user => {
                if(user) {
                    errors.push({ msg: 'Email is already registered.' })
                    res.render('register', {
                        page: 'register',
                        errors,
                        name,
                        email,
                        password,
                        password2
                    })
                } else {
                    const newUser = new User({ name, email, password })

                    // Hash password
                    bcrypt.genSalt(10, (err, salt) => {
                        bcrypt.hash(newUser.password, salt, (err, hash) => {
                            if(err) throw err
                            newUser.password = hash
                            newUser.save()
                                .then(user => {
                                    res.redirect('/users/login')
                                })
                                .catch(err => console.log(err))
                        })
                    })
                }
            })
    }
})

module.exports = router;
