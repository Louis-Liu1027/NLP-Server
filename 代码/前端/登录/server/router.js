let express = require('express')
let router = express.Router()
let login = require('./API/login')
let user = require('./API/user')

router.get('/login', login.login)
router.get('/user', user.user)
router.post('/register', login.register)

module.exports = router
