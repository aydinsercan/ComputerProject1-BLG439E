


<template>
    <form class="login-form">
        <div class="login-container">
        <div class="login-form-group">
            <label for="exampleInputEmail1">Username  </label>
            <input type="email" v-model="form.name" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="login-form-group">
            <label for="exampleInputPassword1">Password  </label>
            <input type="password" v-model="form.password" class="form-control" id="exampleInputPassword1" aria-describedby="passwordHelp" >
            <br>
            <br>
            <router-link to="/user/sign-up">Register </router-link>
        </div>
        <button type="submit" class="login btn btn-primary" @click.prevent="loginUser">LOGIN</button>
        </div>
    </form>
</template>




<script>
export default {    
    data(){
        return{
            form:{
                name:'',
                password:''
            }
        }
    },
    methods:{
        
        async loginUser(){
            

            try{
                await this.$store.dispatch('loginUser', this.form)
                this.$router.push({name: 'myWallet'})
            }
            catch{
                alert('Kullanıcı bilgileri hatalı !')
            }
            
    }
    
}
}
</script>





<style>


.login-container{
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  border: .3rem rgb(59, 111, 18, 0.7) solid;
  border-radius: 6px;
  border-style: outset;
  width: 25%;
  padding: 3rem;
}
.login-form-group{
  width: 90%;
  margin-bottom: 1.2rem;
}

.login.btn.btn-primary{
    width: 90%;
    font-size: 1.3rem;
    font-weight: 500 ;
    background-color: rgb(17, 147, 194)
}




</style>