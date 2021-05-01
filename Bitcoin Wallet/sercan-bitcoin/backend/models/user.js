const mongoose = require('mongoose')
const bcrypt = require('bcrypt')
const bitcoin = require('bitcoinjs-lib');


const userSchema = new mongoose.Schema({

    name:{
        type: String,
        required: true,
        unique:true
    },
    password:{
            type: String,
            required: true,
            minlength: 6,
            trim: true,
    },

    publicKey:{
        type: String,
        trim: true
    },

    privateKey:{
        type: String,
        trim: true
    }
    ,

    balance: {
        type: Number
    }

})




// static means works on model like "User.findBy..." 
userSchema.statics.findByCredentials = async (name, password) =>{

    const user = await User.findOne({ name })

    if(!user){
        throw new Error('Unable to login')
    }

    const isMatch = await bcrypt.compare(password, user.password)

    if(!isMatch){
        throw new Error('unable to login')
    }
    return user
}


userSchema.methods.createKeys = async function(){

    const user = this

    const TestNet = bitcoin.networks.testnet

    let keyPair = bitcoin.ECPair.makeRandom({ network: TestNet });  

    let publicKey = keyPair.publicKey

    let privateKey = keyPair.toWIF();

    let { address } = bitcoin.payments.p2pkh({ pubkey: publicKey,network: TestNet });

    let balance = 0.0000
    user.balance = balance; 

    user.publicKey = address;
    user.privateKey = privateKey;
    

    await user.save() 

}


userSchema.methods.doesPasswordCorrect = async function(password){

    const user = this
    const isMatch = await bcrypt.compare(password, user.password)

    if(!isMatch){
        throw new Error('Şifre doğru değil')
    }else{
        return 'yes'
    }
}



userSchema.pre('save', async function(next){
        
    const user = this

    if (user.isModified('password')){
            user.password = await bcrypt.hash(user.password,8)
    }

    next()
})


const User = mongoose.model('User', userSchema )

module.exports = User
