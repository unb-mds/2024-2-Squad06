import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import Bandeira from '../assets/BandAlagoas.png';
import './SobreProjeto.css';

function SobreProjeto() {
    return (
      <div>
        <Header />
        <div className="SobreProjeto">
          <h1>Sobre o Projeto</h1>
            <p>
            O Monitoramento de Gastos Públicos é uma plataforma desenvolvida para fornecer transparência e facilitar o entendimento sobre as finanças municipais. 
            Seu objetivo é oferecer uma interface acessível e fácil de usar, permitindo que cidadãos, estudantes e profissionais possam visualizar de forma clara e detalhada os padrões de gastos públicos, 
            identificar fornecedores recorrentes e detectar possíveis irregularidades nas contas dos municípios do estado de Alagoas.
            </p>
            <p>
            Através dessa ferramenta, buscamos promover a cidadania ativa e o controle social, garantindo maior visibilidade e compreensão sobre a alocação dos recursos públicos.
            </p>
        
            <h1>Alagoas</h1>
            <p>
                A escolha do estado de Alagoas para a realização deste projeto se dá pela relevância de promover maior transparência na gestão dos recursos públicos em nível municipal. 
                Alagoas, como muitos outros estados brasileiros, enfrenta desafios em relação à fiscalização das finanças públicas, o que dificulta o acompanhamento da população e de profissionais que buscam entender e monitorar os gastos do governo.
            </p>
            <p>
                Nosso objetivo é contribuir para o fortalecimento da cidadania ativa e do controle social, proporcionando maior transparência e compreensão sobre a alocação dos recursos públicos no estado de Alagoas.
            </p>
            <img src={Bandeira} className='Band-Alagoas' alt='Bandeira Alagoas' />
            

        </div>

        <Footer />

      </div>
    );
  }

  export default SobreProjeto;