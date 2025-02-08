import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

function SobreNos() {
    return (
      <div>
        <Header />
        <div className="flex flex-col justify-start items-center py-0 px-[1.25rem] text-left bg-white my-[1.25rem]">
          <div>
            <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Sobre Nós</h1>
            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
              Somos um grupo de estudantes da Universidade de Brasília (UnB), envolvidos na disciplina de Modelagem e Desenvolvimento de Sistemas (MDS). 
              Nosso principal objetivo é criar soluções inovadoras que melhorem a gestão de processos e recursos em diferentes tipos de organizações.
            </p>
            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
                Trabalhamos aplicando técnicas de desenvolvimento de sistemas que garantem integração e automação de processos, 
                além de garantir que as informações estejam sempre organizadas e facilmente acessíveis.
                Acreditamos que, ao usar a tecnologia de forma estratégica, podemos ajudar a melhorar o desempenho de organizações, seja em pequenos negócios ou grandes empresas.
            </p>
            <p className="text-[1.2rem] leading-[1.6] mb-[1.5rem] max-w-[50rem] w-full">
                Nosso time é composto por estudantes apaixonados por tecnologia, sempre em busca de novos desafios que possam aprimorar tanto o ambiente corporativo quanto acadêmico.
            </p>
            <p className="text-[1.2rem] leading-[1.6] mb-[1.5rem] max-w-[50rem] w-full">
                Para mais informações sobre o nosso projeto, visite nossa{" "}
                <a href="https://unb-mds.github.io/2024-2-Squad06/" className="text-blue-600">GitPage</a>.
            </p>
          </div>
          <div>''
          <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Sobre a FCTE</h1>

            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
              A Faculdade de Ciências e Tecnologias em Engenharia(FCTE) foi criada com o objetivo de expandir o ensino superior, 
              com foco na formação de engenheiros com uma visão crítica e humanista.
            </p>
            <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
              A FCTE oferece cursos de Engenharia Aeroespacial, Automotiva, de Energia, Eletrônica e de Software, com ênfase na interdisciplinaridade, 
              pesquisa e inovação tecnológica. Os cursos têm duração de cinco anos, com um currículo que inclui disciplinas teóricas e práticas, além de atividades de pesquisa e extensão.
            </p>

            <img className="block mx-auto w-[60%] max-w-[100%] p-[1.25rem]" src="/assets/FCTE.jpg" alt="FCTE" />
          </div>

        </div>

        <Footer />

      </div>
    );
  }

  export default SobreNos;