import React from 'react';
import './SobreNos.css';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

function SobreNos() {
    return (
      <div>
        <Header />
        <div className="SobreNos">
          <div>
            <h1>Sobre Nós</h1>
            <p>
                Somos um grupo de estudantes da Universidade de Brasília (UnB), atuando na disciplina de Modelagem e Desenvolvimento de Sistemas (MDS). 
                Nosso objetivo é criar soluções inovadoras para otimizar a gestão de processos e recursos em diferentes tipos de organizações. 
            </p>
            <p>
                Nosso trabalho é baseado na aplicação de técnicas de modelagem e desenvolvimento de sistemas que garantam a integração e a automação de processos, 
                além de assegurar que as informações estejam sempre acessíveis e bem organizadas. 
                Acreditamos que, com o uso estratégico da tecnologia, é possível impactar positivamente o desempenho organizacional, seja em pequenas empresas ou grandes corporações.
            </p>

            <p>
                Nosso time é formado por estudantes dedicados, 
                apaixonados por tecnologia e em busca de desafios que contribuam para o aprimoramento do ambiente corporativo e acadêmico.
            </p>
          </div>
          <div>
          <h1>Sobre a FCTE</h1>

            <p>
              A Faculdade de Ciências e Tecnologias em Engenharia(FCTE) foi criada com o objetivo de expandir o ensino superior, 
              com foco na formação de engenheiros com uma visão crítica e humanista.
            </p>
            <p>
              A FCTE oferece cursos de Engenharia Aeroespacial, Automotiva, de Energia, Eletrônica e de Software, com ênfase na interdisciplinaridade, 
              pesquisa e inovação tecnológica. Os cursos têm duração de cinco anos, com um currículo que inclui disciplinas teóricas e práticas, além de atividades de pesquisa e extensão.
            </p>

            <img id="AboutFCTE" src="/assets/FCTE.jpg" alt="FCTE" />
          </div>

        </div>

        <Footer />

      </div>
    );
  }

  export default SobreNos;