const express = require('express');
const router = new express.Router();
const User = require('../models/user')


// creates new user in database
router.post('/user/create', async (req, res)=>{
   
    try{

    const form = req.body

    if(form.password.length >= 6){

        if(form.password === form.passwordAgain)
        {
            const isUnique = await User.findOne({name: form.name})
            if( isUnique === null){
                const user = new User(form)
                await user.save()
                await user.createKeys()
    
                res.send('Kullanıcı profili oluşturuldu !')
            }else{

                throw new Error('Bu isimle kayıtlı kullanıcı zaten var ! ')

            }

        }
        else if(form.password !== form.passwordAgain){

            throw new Error('Şifre ile tekrarı uyuşmuyor!')
        }
        }
        else{
       
            throw new Error("parola '6' haneden az olmamalı !")
        }

    }catch(e){

         res.send(e.message)

    }
})


// check if login successful or not 
router.post('/user/login', async (req, res) =>{
    try{

        const user = await User.findByCredentials(req.body.name, req.body.password)
        res.send(user)

    }
    catch(e){
        res.status(400).send(e)
    }
})


module.exports = router
