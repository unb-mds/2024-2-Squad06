import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

function SobreProjeto() {
    return (
      <div>
        <Header />
        <div className="flex flex-col justify-start items-center px-[1.25rem] text-left bg-white my-[1.25rem]">
          <h1 className="text-[2.5rem] mb-[1.25rem]">Sobre o Projeto</h1>
            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[50rem] w-full">
            O Monitoramento de Gastos Públicos é uma plataforma desenvolvida para fornecer transparência e facilitar o entendimento sobre as finanças municipais. 
            Seu objetivo é oferecer uma interface acessível e fácil de usar, permitindo que cidadãos, estudantes e profissionais possam visualizar de forma clara e detalhada os padrões de gastos públicos, 
            identificar fornecedores recorrentes e detectar possíveis irregularidades nas contas dos municípios do estado de Alagoas.
            </p>
            <p className="text-[1.2rem] leading-[1.6] mb-[1.5rem] max-w-[50rem] w-full">
            Através dessa ferramenta, buscamos promover a cidadania ativa e o controle social, garantindo maior visibilidade e compreensão sobre a alocação dos recursos públicos.
            </p>
        
            <h1 className="text-[2.5rem] mb-[1.25rem]">Alagoas</h1>
            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[50rem] w-full">
                A escolha do estado de Alagoas para a realização deste projeto se dá pela relevância de promover maior transparência na gestão dos recursos públicos em nível municipal. 
                Alagoas, como muitos outros estados brasileiros, enfrenta desafios em relação à fiscalização das finanças públicas, o que dificulta o acompanhamento da população e de profissionais que buscam entender e monitorar os gastos do governo.
            </p>
            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[50rem] w-full">
                Nosso objetivo é contribuir para o fortalecimento da cidadania ativa e do controle social, proporcionando maior transparência e compreensão sobre a alocação dos recursos públicos no estado de Alagoas.
            </p>
            <img src='/assets/BandAlagoas.png' className='p-[1.25rem]' alt='Bandeira Alagoas' />
        </div>
        <Footer />
      </div>
    );
  }

  export default SobreProjeto;