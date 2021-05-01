<template>
   <header class="header"> 

            <div class="brand">
                 <router-link to="/" class="user-entrance-route">
                <a href="/"> Bitcoin  <i class="fab fa-btc"></i> </a>
                 </router-link>
            </div>

        </header>
</template>

<script>

export default {
    name: 'Header'
}

</script>

<style>


.header{
    font-family: 'Ubuntu', sans-serif;
    grid-area: header;
    position: fixed;
    width: 100%;
    height: 4rem;
    background-color:  rgb(23, 124, 123);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding-left: 2rem;

}

.burger{
    border: .1rem rgb(255, 255, 255) solid;
    cursor: pointer;
}

.burger div{
    width: 33.75px;
    height: 0.16rem;
    background-color: white;
    margin: 6.25px;
    transition: all 0.3s ease;
}


.brand{
    flex: 1 1 50%;
}

.brand a{
    color: white;
    text-decoration: none;
    font-size: 2.8rem;
    padding-left: 6rem;
}

.brand a:hover{
    color: #f0fd00;
    text-decoration: none;
}

.costumer-service{
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 2 2 35%;
}

#but{
    font-size: 2rem;
}

.costumer-service .user-entrance{
    color: white;
    text-decoration: none;
    font-size: 2rem;
    padding-right: 2rem;
    padding-left: 1.3rem;
}
.costumer-service .user-entrance:hover{
    color: #f0fd00;
    text-decoration: none;
}

    

.btn.btn-secondary{
    background-color: rgb(255, 181, 43);
    height: 3rem;
    width: 10rem;
    font-size: 1.5rem;
    font-weight: 500;
    border-radius: 12.5px;
    color: rgb(20, 102, 255)
}
.btn.btn-secondary:hover{
    background-color: orangered ;
    color: white;
}

.btn.btn-secondary.active.focus, .btn.btn-secondary.active:focus,
.btn.btn-secondary.focus, .btn.btn-secondary:active.focus, 
.btn.btn-secondary:active:focus, .btn.btn-secondary:focus {
  outline: none;
  box-shadow: none;

}

.user-entrance-route:hover{
    text-decoration: none;
}
a {
  text-decoration: none;
}

.dropdown-bla{
    height: 10vh;
    background-color: none;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.projects{
  position: relative;
}

.projects li{
    background-color: rgb(92, 189, 124);
    width: 100%;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.projects li:hover{
        background-color: rgb(61, 151, 91);
}

.projects li a:hover{
        color:  white;
        text-decoration: none;
}

.projects ul{
    position: absolute;
    list-style: none;
    background-color:wheat;
    width: 130px;
    right: 0px;
    margin-top: 6px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
    opacity: 0;
    transition: all 0.4s ease;
    visibility: hidden;
  
}


.dropdown-bla .projects button{
    background: none;
    border: none;    
    color: white;
    font-size: 18px;
    cursor: pointer;
}

.dropdown-bla button:hover{
    color: #f0fd00;
}

.projects button:focus + ul{
     opacity: 1;
     visibility: visible;
}

.projects button:focus{
     outline: none;
     box-shadow: none;
}
@media (max-width: 1500px) {

    
.navLinks {
    position: fixed;
    top: 3rem;
    bottom: 1.7rem;
    width: 15rem;
    left: 0px;
    background-color: rgb(21, 136, 136, 0.7);
    display: flex;
    flex-direction: column;
    transform: translateX(-100%);
    transition: transform 0.5s ease-in;
    justify-content: space-evenly;
}

.nav-active{
    transform: translateX(0%);
}

.navLinks li{
    padding: 0 2rem; 
    opacity: 0;
    list-style-type: none;
}

.navLinks a{
    font-size: 2rem;
    text-decoration: none;
    color: white;
}
.navLinks a:hover{
    font-size: 2rem;
    text-decoration: none;
    color: #f0fd00;
}

@keyframes navLinkFade {
    from {opacity: 0;
          transform: translateX(-50px);      
        }
    to {opacity: 1;
        transform: translateX(0px);      
      }
  }

  .toggle .line1{
      transform: rotate(-45deg) translate(-4px,5px);
      
  }
  .toggle .line2{
    opacity: 0;
    }
    .toggle .line3{
        transform: rotate(45deg) translate(-4px,-5px);
    
    }

.header{
    font-family: 'Ubuntu', sans-serif;
    grid-area: header;
    position: fixed;
    width: 100%;
    height: 3.2rem;
    background-color:  rgb(21, 136, 136);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding-left: 2rem;

}

.burger{
    border: .1rem rgb(255, 255, 255) solid;
    cursor: pointer;
}

.burger div{
    width: 28px;
    height: 0.16rem;
    background-color: white;
    margin: 5px 5px;
    transition: all 0.3s ease;
}


.brand{
    flex: 1 1 50%;
}

.brand a{
    color: white;
    text-decoration: none;
    font-size: 2.5rem;
    padding-left: 6rem;
}

.brand a:hover{
    color: #f0fd00;
    text-decoration: none;
}

.costumer-service{
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 2 2 35%;
}

#but{
    font-size: 1.8rem;
}

.costumer-service .user-entrance{
    color: white;
    text-decoration: none;
    font-size: 1.8rem;
    padding-right: 2rem;
    padding-left: 1.3rem;
}
.costumer-service .user-entrance:hover{
    color: #f0fd00;
    text-decoration: none;
}

    

.btn.btn-secondary{
    background-color: rgb(255, 181, 43);
    height: 2.5rem;
    width: 10rem;
    font-size: 1.5rem;
    font-weight: 500;
    border-radius: 10px;
    color: rgb(20, 102, 255);
    padding-top: .1rem;
    
}
.btn.btn-secondary:hover{
    background-color: orangered ;
}

.btn.btn-secondary.active.focus, .btn.btn-secondary.active:focus,
.btn.btn-secondary.focus, .btn.btn-secondary:active.focus, 
.btn.btn-secondary:active:focus, .btn.btn-secondary:focus {
  outline: none;
  box-shadow: none;

}

.user-entrance-route:hover{
    text-decoration: none;
}
a {
  text-decoration: none;
}

.dropdown-bla{
    background-color: none;
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 1rem;
}

.projects{
  position: relative;
}

.projects li{
    background-color: rgb(92, 189, 124);
    width: 100%;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.projects li:hover{
        background-color: rgb(61, 151, 91);
}

.projects li a:hover{
        color:  white;
        text-decoration: none;
}

.projects ul{
    position: absolute;
    list-style: none;
    background-color:wheat;
    margin-top: 2px;
    width: 130px;
    right: 0px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
    opacity: 0;
    transition: all 0.4s ease;
    visibility: hidden;
  
}


.dropdown-bla .projects button{
    background: none;
    border: none;    
    color: white;
    font-size: 18px;
    cursor: pointer;
}

.dropdown-bla button:hover{
    color: #f0fd00;
}

.projects button:focus + ul{
     opacity: 1;
     visibility: visible;
}

.projects button:focus{
     outline: none;
     box-shadow: none;
}
}

</style>