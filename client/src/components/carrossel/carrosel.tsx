import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Carousel from 'react-bootstrap/Carousel';
import './carroselStyle.css';

export default function Carrossel() {
  const imagens = [
    { src: '/assets/ponta_alagoas.png', alt: 'ponta_alagoas', 
      texto: 'O que são gastos públicos?',corpo:"É o processo pelo qual a Administração Pública gerencia e aloca recursos financeiros para cumprir suas responsabilidades. Em outras palavras, os gastos públicos representam como o governo investe os recursos arrecadados em áreas essenciais, como saúde, educação, segurança e infraestrutura." ,
      transcicao:"" },
    { src: '/assets/gastos.png', alt: 'gastos', 
      texto: 'Texto sobre a imagem',corpo:"texto de explicação", 
      transcicao:"" },
    { src: '/assets/monitoramento.png', alt: 'monitoramento', 
      texto: 'Texto sobre a imagem',corpo:"texto de explicação",
      transcicao:""  },
    { src: '/assets/grupo.png', alt: 'grupo', 
      texto: 'Texto sobre a imagem',corpo:"texto de explicação",
      transcicao:"" },
  ];

  return (
    <div className="carrossel-container" >
      <Carousel fade>
        {imagens.map((imagem, index) => (
          <Carousel.Item key={index}>
            <div className="carousel-item-container" >
              <img
                src={imagem.src}
                alt={imagem.alt}
                className="carousel-item-image"/>
              <div className="carousel-item-transcicao">
                {imagem.transcicao}
              </div>
              <div className="carousel-item-text">
                {imagem.texto}
              </div>
              <div className="carousel-item-body">
                {imagem.corpo}
              </div>
            </div>
          </Carousel.Item>
        ))}
      </Carousel>
    </div>
  );
}
