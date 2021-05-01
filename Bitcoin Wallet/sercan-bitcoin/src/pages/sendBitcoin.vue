<template>

    <div  class="product-card">

        <div class="headSendBit">
            <p >Send Bitcoin</p>
        </div>

        <form class="sendBit-container">
                <div class="form-group-sendBitcoin">
                    <label for="receivedAddress">Reciever Address : </label>
                    <input v-model="form.address" class="form-control" id="receivedAddress">
                </div>

                <div class="form-group-sendBitcoin">
                    <label for="amountBitcoin">Amount : </label>
                    <input v-model="form.amount" class="form-control" id="amountBitcoin">
                </div>

        </form>
        

        
        <div class="cart-buttons"  >
                <button @click.prevent="sendBitcoin" class="login btn btn-success sendBitcoin" href="#" variant="primary">Send</button>
        </div>


    </div>

</template>


<script>

var bitcoin = require('bitcore-lib');

var explorers = require('bitcore-explorers');
var insight = new explorers.Insight();


export default {
    name: 'myWallet',


    data(){

        return{

            form:{
                address:'',
                amount:'',
                privateKey : this.$store.state.privateKey,
                publicKey : this.$store.state.publicKey
            }

        }

    }
    ,

    methods:{

        sendBitcoin() {
            var address = bitcoin.Address;
            var str = this.form.address;
            if(address.isValid(str)){
                alert('Bitcoin is sended to TestNet');
                insight.getUtxos(this.form.publicKey, (err, utxos) => {
                    let tx = bitcoin.Transaction();
                    tx.from(utxos);
                    tx.to(this.form.address, this.form.amount);
                    tx.change(this.form.publicKey);
                    tx.sign(this.form.privateKey);
                    tx.fee(fee);
                    tx.serialize();

                    insight.broadcast(tx.toString(), (error, txid) => {
                        if (error) 
                        {
                            alert(error)
                        } 
                        else 
                        {
                            console.log(txid) //Transaction id
                        }
                    })
                });
            }
            else{
                alert('INVALID receiver Public Key');
                location.reload();

            }
        }
    },

    computed:{

    }

}
</script>

<style>

.sendBit-container{
    width: 80%;
}

.form-group-sendBitcoin{
  width: 90%;
  margin-bottom: 1.2rem;
}


.headSendBit{
    width: 100%;
    height: 5rem;
    color: rgb(45, 78, 109);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom:3rem;
    padding-top: 0.5rem;
    font-size: 3rem;
    font-weight: 600;
    margin-top: 0.5rem;
}

.product-card {

  font-family:'Poppins', sans-serif;   
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 2px 2px 3px 2px rgb(206, 156, 156);
  height: 35%;
  width: 40%;
}



.product-price{
    font-size: 1.7rem ;
    font-weight: 600;
    color: rgb(255, 103, 48);
    margin-bottom: 4rem;
    text-align: center;
}

@media (max-width: 1500px) {

.headSendBit{
width: 100%;
height: 3.5rem;
display: flex;
align-items: center;
justify-content: center;
margin-bottom:1.5rem;
font-size: 2.5rem;
margin-top: 0.5rem;
}

.product-card {
   
  font-family:'Poppins', sans-serif;   
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex; /* so child elements can use flexbox stuff too! */
  flex-direction: column;
  align-items: center;
  box-shadow: 2px 2px 3px 2px rgb(206, 156, 156);
  height: 55%;
  width: 70%;
 
 
}


.product-price{
    font-size: 1.3rem ;
    font-weight: 600;
    color: rgb(255, 103, 48);
    margin-bottom: 2rem;
    text-align: center;
}
}

/* buttons */

.cart-buttons{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
}


.sendBitcoin{
    flex-basis: 20%;
    align-items: center;
}

.askBitcoin{
    flex-basis: 20%; 
     align-items: center;
}

.btn.buy.btn-primary{
    background-color: rgb(255, 166, 0);
    font-size: 1.rem;
}

.btn.arrange.btn-primary{
   background-color : #007bff ;
}
.btn.remove.btn-primary{
    background-color: rgb(243, 45, 45) ;
}

</style>