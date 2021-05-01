import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)


export default new Vuex.Store({

    state:{
        publicKey: null,
        privateKey: null,
        balance: null
        },
    
    mutations:{

        LOGIN_USER(state,  {publicKey, privateKey, balance} ){

            state.publicKey = publicKey
            state.privateKey = privateKey
            state.balance = balance

            
        }
        
    },


    getters:{
        

        getPublicKey : state => {
            return state.user.publicKey
        },
        getPrivateKey : state => {
            return state.user.privateKey
        }


    },

    actions:{
        
        loginUser({commit}, form){

            return new Promise( (resolve, reject) => {

            axios.post('http://localhost:5000/user/login', form)

            .then(( res ) => {

               
                const publicKey = res.data.publicKey
                const privateKey = res.data.privateKey
                const balance = res.data.balance

                
                commit('LOGIN_USER', {publicKey, privateKey, balance})

                console.log(publicKey, privateKey, balance)

                resolve(res)

            })
            .catch( (e)=> {  reject(e) } )

            

            })
           
        },


        }

})