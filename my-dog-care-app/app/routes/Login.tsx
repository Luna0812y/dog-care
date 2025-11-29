

import '../assets/css/Adjusts.css'
import "../assets/css/Flex.css"
import '../assets/css/General.css'
import '../assets/css/LoginForm.css'

import ReturnBtn from './ReturnBtn'
import {Link} from 'react-router'

const Login = (): React.ReactElement => {
    return (
        <>
          <div id="login-form-area" className="flex column going-center mh">
            <div id="login-form-area-within">
                <h2 id="post-login-title">Olá, tutor! faça o login</h2>

                <form action="#">
                  <div className="flex column going-center gap-md">
                    <input className="ordinary-input-b" type="text" placeholder="Seu nome de tutor" required/>
                    <input className="ordinary-input-b" type="text" placeholder="Senha" required/>
                    <div className='flex row going-center'>
                        {/* <button type="submit" id="post-login-within-btn">entrar</button> */}
                        <Link to="/pet-owner-panel" id="post-login-within-btn">entrar</Link>
                        <ReturnBtn/>
                    </div>
                  </div>
                </form>
            </div>
          </div>
        </>
    )
}

export default Login