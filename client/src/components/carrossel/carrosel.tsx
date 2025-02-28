import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Carousel from 'react-bootstrap/Carousel';

export default function Carrossel() {
  const imagens = [
    { 
      src: '/assets/ponta_alagoas.png', alt: 'ponta_alagoas', 
      texto: 'O que são gastos públicos?', corpo:"É o processo pelo qual a Administração Pública gerencia e aloca recursos financeiros para cumprir suas responsabilidades. Em outras palavras, os gastos públicos representam como o governo investe os recursos arrecadados em áreas essenciais, como saúde, educação, segurança e infraestrutura." ,
      transcicao:"" 
    },
    { 
      src: '/assets/gastos.png', alt: 'gastos', 
      texto: 'Gastos Públicos', corpo:"Gastos públicos são os recursos que o governo usa para financiar serviços essenciais, infraestrutura, projetos sociais e o pagamento de dívidas, sendo financiados pela arrecadação de impostos e contribuições, visando garantir o funcionamento do Estado e o bem-estar da sociedade.", 
      transcicao:"" 
    },
    { 
      src: '/assets/monitoramento.png', alt: 'monitoramento', 
      texto: 'Monitoramento', corpo:"O monitoramento dos gastos públicos foi feito por meio da análise da API do Querido Diário, que forneceu dados essenciais sobre contratos, fornecedores e transações. Foram avaliados pontos como nome do fornecedor, datas de assinatura, vigência dos contratos, CNPJ e valores, com foco na transparência e legalidade das transações.",
      transcicao:""  
    },
    { 
      src: '/assets/grupo.png', alt: 'grupo', 
      texto: 'Sobre o Projeto', corpo:"O Monitoramento de Gastos Públicos é uma plataforma que facilita a visualização e compreensão das finanças municipais em Alagoas, permitindo identificar padrões de gastos, fornecedores recorrentes e irregularidades, promovendo a cidadania ativa e o controle social.",
      transcicao:"" 
    },
  ];

  return (
    <div className="relative mx-auto px-4 mt-10 mb-10 w-[90%] max-w-[60rem]">
      <Carousel fade>
        {imagens.map((imagem, index) => (
          <Carousel.Item key={index}>
            <div className="relative w-full h-[20rem]">
              <img
                src={imagem.src}
                alt={imagem.alt}
                className="w-full h-full object-cover"
              />
              <div className="absolute bottom-0 left-0 w-full h-[15%] bg-[#112632]"></div>
              <div 
                className="absolute bottom-[15%] left-0 w-full h-[100%]"
                style={{
                  background: 'linear-gradient(to top, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 100%)'
                }}
              ></div>
              <div className="absolute bottom-[15%] left-0 p-[2.5%] w-full">
                <div className="text-2xl font-bold text-black ">
                  {imagem.texto}
                </div>
                <div className="mt-2 text-m overflow-y-auto max-h-[10rem]">
                  {imagem.corpo}
                </div>
              </div>
            </div>
          </Carousel.Item>
        ))}
      </Carousel>
      <style>{`
        .carousel-control-prev, .carousel-control-next {
          position: absolute;
          bottom: 0.5rem; 
          top: auto;  
          z-index: 10;
          
        }

        .carousel-control-prev {
          left: 0.5rem;  
        }

        .carousel-control-next {
          right: 0.5rem;
        }
        
        @media (max-width: 800px) {
          .carousel-control-prev, .carousel-control-next {
            width: 1.8rem;
            height: 1.8rem;
          }
        }
        
      `}</style>
    </div>
  );
}
