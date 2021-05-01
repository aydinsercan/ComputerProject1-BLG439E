import Login from './pages/Login'
import SignUp from './pages/SignUp'
import myWallet from './pages/myWallet'
import sendBitcoin from './pages/sendBitcoin'
import askBitcoin from './pages/askBitcoin'

export default [

    {
        path: '/',
        component: Login,
        name: 'login'
    },
    
    {
        path: '/user/myWallet',
        component: myWallet,
        name: 'myWallet'
    },
    
    {
        path: '/user/sign-up',
        component: SignUp,
        name: 'signUp'
    }
    ,

    {
        path: '/user/send-bitcoin',
        component: sendBitcoin,
        name: 'sendBitcoin'
    }

    ,

    {

        path: '/user/ask-bitcoin',
        component: askBitcoin,
        name: 'askBitcoin'

    }

]