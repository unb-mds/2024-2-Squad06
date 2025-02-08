import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

function SobreProjeto() {
  return (
    <div>
      <Header />
      <div className="flex flex-col justify-start items-center px-[1.25rem] text-left bg-white my-[1.25rem]">
        <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Sobre o Projeto</h1>
        <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
          O Monitoramento de Gastos Públicos é uma plataforma desenvolvida para fornecer transparência e facilitar o entendimento sobre as finanças municipais. 
          Seu objetivo é oferecer uma interface acessível e fácil de usar, permitindo que cidadãos, estudantes e profissionais possam visualizar de forma clara e detalhada os padrões de gastos públicos e 
          identificar fornecedores recorrentes nas contas do município de Maceió.
        </p>
        <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
          Através dessa ferramenta, buscamos promover a cidadania ativa e o controle social, garantindo maior visibilidade e compreensão sobre a alocação dos recursos públicos.
        </p>
        <div>
          <h1 className="text-[2.5rem] mb-[1.25rem] text-center">O que são Gastos públicos?</h1>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            Gastos públicos referem-se ao dinheiro que o governo utiliza para financiar as suas atividades, como a prestação de serviços públicos (saúde, educação, segurança), infraestrutura, investimentos em projetos sociais e o pagamento de dívidas. 
            Esses gastos são realizados com recursos obtidos por meio da arrecadação de impostos, taxas e contribuições, e são essenciais para garantir o funcionamento do Estado e o bem-estar da sociedade.
          </p>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            Além disso, a gestão eficiente dos gastos públicos é crucial para o desenvolvimento econômico e social, 
            garantindo que os recursos sejam alocados de forma responsável e que as políticas públicas atendam às necessidades da população de maneira justa e eficaz. O controle e a transparência nos gastos públicos são fundamentais para evitar desperdícios, 
            combater a corrupção e assegurar que os recursos sejam utilizados de acordo com o interesse público.
          </p>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            Para garantir o uso responsável e eficiente dos recursos públicos, é fundamental que a população compreenda alguns pontos essenciais. A seguir, destacamos aspectos importantes que envolvem a gestão dos gastos públicos e sua relação com a sociedade.
          </p>
        </div>
        <div className="w-full max-w-4xl text-center">
          <ul className="list-disc text-lg leading-7 text-left mx-auto mb-4 w-auto">
            <li className="mb-3 text-black">
              <strong>Transparência:</strong> A população deve exigir clareza na gestão dos recursos públicos para garantir eficiência e evitar desperdícios.
            </li>
            <li className="mb-3 text-black">
              <strong>Impostos:</strong> Os impostos pagos pela sociedade financiam os serviços públicos, por isso, é importante entender como o governo utiliza esse dinheiro.
            </li>
            <li className="mb-3 text-black">
              <strong>Orçamento e Prioridades:</strong> O governo define suas prioridades no orçamento, e é essencial que a população compreenda onde o dinheiro será investido.
            </li>
            <li className="mb-3 text-black">
              <strong>Dívidas públicas:</strong> Parte dos gastos é destinada ao pagamento de dívidas, o que pode impactar outras áreas e políticas fiscais.
            </li>
            <li className="mb-3 text-black">
              <strong>Participação cidadã:</strong> A população pode influenciar nas decisões sobre o uso dos recursos públicos, garantindo um uso responsável e eficaz do dinheiro arrecadado.
            </li>
          </ul>
        </div>
        <div>
          <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Monitoramento</h1>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            O monitoramento dos gastos públicos foi realizado por meio da análise da API do Querido Diário. 
            Essa ferramenta foi fundamental para obter informações detalhadas sobre os contratos e transações no setor público, 
            permitindo identificar padrões importantes nos dados. Com uma observação cuidadosa, foi possível organizar as informações de forma mais clara e estruturada.
          </p>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            Aqui estão os principais pontos-chave utilizados para o monitoramento:
          </p>
        </div>
        <div className="w-full max-w-4xl text-center">
          <ul className="list-disc text-lg leading-7 text-left mx-auto mb-4 w-auto">
            <li className="mb-3 text-black">
              <strong>Nome do Fornecedor:</strong> A API forneceu acesso aos nomes dos fornecedores envolvidos nas transações, 
              o que foi fundamental para entender quem eram as empresas responsáveis pelos serviços ou produtos adquiridos.
            </li>
            <li className="mb-3 text-black">
              <strong>Data de Assinatura e Publicação:</strong> As datas de assinatura e publicação dos contratos foram analisadas 
              para garantir que tudo estivesse sendo feito dentro dos prazos estabelecidos pela lei, o que também reforça a transparência nesse processo.
            </li>
            <li className="mb-3 text-black">
              <strong>Vigência:</strong> Também foi dada atenção à vigência dos contratos, para verificar os períodos de validade e execução dos serviços ou fornecimentos, 
              ajudando a manter o controle sobre o que estava sendo acordado.
            </li>
            <li className="mb-3 text-black">
              <strong>CNPJ:</strong> O CNPJ dos fornecedores foi um dado chave para assegurar que as empresas envolvidas nas transações estavam devidamente registradas, 
              o que garante a legalidade de todo o processo.
            </li>
            <li className="mb-3 text-black">
              <strong>Valores:</strong> A análise dos valores foi crucial para entender o quanto estava sendo gasto em cada transação. Isso permitiu comparar diferentes contratos 
              e identificar possíveis inconsistências ou áreas que precisavam de mais atenção.
            </li>
          </ul>
        </div>
        <div>
          <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Maceió</h1>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            A escolha da cidade de Maceió para a realização deste projeto se dá pela relevância de promover maior transparência na gestão dos recursos públicos em nível municipal. Maceió, como muitas outras cidades brasileiras, 
            enfrenta desafios em relação à fiscalização das finanças públicas, o que dificulta o acompanhamento da população e de profissionais que buscam entender e monitorar os gastos do governo.
          </p>
          <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
            Nosso objetivo é contribuir para o fortalecimento da cidadania ativa e do controle social, proporcionando maior transparência e compreensão sobre a alocação dos recursos públicos no município de Maceió.
          </p>
          <img src='/assets/BandAlagoas.png' className='p-[1.25rem] mx-auto' alt='Bandeira Alagoas' />
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default SobreProjeto;
