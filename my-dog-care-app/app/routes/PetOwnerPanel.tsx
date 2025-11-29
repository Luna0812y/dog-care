

import '../assets/css/Adjusts.css'
import '../assets/css/Flex.css'
import '../assets/css/PetOwnerPanel.css'

import PetPostForm from './PetPostForm';

// import {Link} from 'react-router'
import { useState } from 'react';

const PetOwnerPanel = (): React.ReactElement => {
  const [mostrarForm, setMostrarForm] = useState(false);

  return (
    <div id="container" className='flex column going-center gap-sm mh'>
      <h1 id="user-area">Área do usuário</h1>
      <div id="labels-area" className="flex row going-center gap-lg">
        <p id="pet-logo">🐶</p>
        <h2>Seus pets</h2>
      </div>

      {/* Aqui, seria a div p/ inserir os dados dinâmicos */}
      <div id="pets-from-user-session" className='flex row going-left gap-sm'>
          <div className="pet-card flex column gap-sm">
            <p className="pet-name">Nome: Tonhão</p>
            <p className="pet-breed">Raça: Beagle</p>
            <p className="pet-register-date">Registro: 09/10/2025</p>
            <p className="pet-birth">Nascimento: 12/02/2021</p>
          </div>
          <div className="pet-card flex column gap-sm">
            <p className="pet-name">Nome: Roberto Carlos</p>
            <p className="pet-breed">Raça: Golden Retriever</p>
            <p className="pet-register-date">Registro: 17/10/2025</p>
            <p className="pet-birth">Nascimento: 26/08/2019</p>
          </div>
      </div>

      <button id="add-new-pet-form-btn" onClick={() => setMostrarForm(!mostrarForm)}>✚</button>

      {mostrarForm && (
        <PetPostForm/>
      )}

    </div>
  )
}

export default PetOwnerPanel
