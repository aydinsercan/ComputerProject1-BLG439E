<template>

<div class="ask-bitcoin-container">

       <div  id="ask-bitcoin-card">

        <div id="QR-code-img">
            <img src="https://www.investopedia.com/thmb/ZG1jKEKttKbiHi0EkM8yJCJp6TU=/1148x1148/filters:no_upscale():max_bytes(150000):strip_icc()/qr-code-bc94057f452f4806af70fd34540f72ad.png" alt="qr-code-img">
        </div>
    
        <div id="public-key">
            <p> {{publicKey}} </p>
        </div>
    </div>

</div>
 
</template>


<script>


export default {
    name: 'myWallet',
    


    data(){

        return{

            publicKey : this.$store.state.publicKey

        }

    }
    ,

    methods:{

    },

    computed:{

    }

}
</script>


<style>



#ask-bitcoin-card{

  font-family:'Poppins', sans-serif;   
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: 2px 2px 3px 2px rgb(128, 104, 104);
  height: 30rem;
  width: 30rem;
  padding-top: 3.5rem;
}

#public-key{
    font-size: 1.2rem ;
    font-weight: 600;
    color: rgb(255, 0, 0);
    margin-bottom: 4rem;
    text-align: center;
    margin-top: 1rem;
}

#QR-code-img img{
    width: 100%;
}

#QR-code-img{
    width: 80%;
}
@media (max-width: 1500px) {
#ask-bitcoin-card{

  font-family:'Poppins', sans-serif;   
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: 2px 2px 3px 2px rgb(128, 104, 104);
  height: 30rem;
  width: 30rem;
  padding-top: 3.5rem;
}

#public-key{
    font-size: 1.2rem ;
    font-weight: 600;
    color: rgb(255, 0, 0);
    margin-bottom: 4rem;
    text-align: center;
    margin-top: 1rem;
}

#QR-code-img img{
    width: 100%;
}

#QR-code-img{
    width: 80%;
}

}

</style>