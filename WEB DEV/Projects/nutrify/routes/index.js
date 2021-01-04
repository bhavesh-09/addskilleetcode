const express = require('express')
const router = express.Router()

router.get('/', (req, res) => res.render('login', {page: 'login'}))
router.get('/tracker', (req, res) => res.render('tracker', {page: 'tracker'}))

module.exports = router;