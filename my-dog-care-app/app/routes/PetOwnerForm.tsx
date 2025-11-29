

import '../assets/css/Flex.css'
import '../assets/css/General.css'
import '../assets/css/PetOwnerForm.css'

const PetOwnerForm = (): React.ReactElement => {
    return (
        <>
          <div id="pet-owner-form-area" className="flex column going-center gap-lg">
            <div>
              <h2 id="post-pet-owner-title">Cadastre-se como Tutor</h2>
            </div>

            <form action="#">
              <div className="flex column going-left gap-md">
                <input className="ordinary-input" type="text" placeholder="Seu nome de tutor" required/>
                <input className="ordinary-input" type="email" placeholder="Seu e-mail" required/>
                <input className="ordinary-input" type="text" placeholder="Senha" required/>
                <button id="post-new-pet-owner-btn">cadastrar</button>
              </div>
            </form>
            
          </div>
        </>
    )
}

export default PetOwnerForm
