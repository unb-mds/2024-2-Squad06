import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="App-footer">
      <div className="logo-container">
          <img src="/assets/logo.png" className="App-logo" alt="logo" />
          <div id="title">Gastos Públicos</div>
      </div>
      <ul className="navigation__footer">
          <li><a className="navigation__footer__link" href="" target="_blank" rel="noopener noreferrer">Gastos</a></li>
          <li><a className="navigation__footer__link" href="" target="_blank" rel="noopener noreferrer">Monitoramento</a></li>
          <li><a className="navigation__footer__link" href="" target="_blank" rel="noopener noreferrer">Sobre o projeto</a></li>
          <li><a className="navigation__footer__link" href="" target="_blank" rel="noopener noreferrer">Sobre nós</a></li>
        </ul>
      <div>
        <img src="/assets/logoUnb.png" className="Unb-logo" alt="logo" />
      </div>
    </footer>
  );
}

export default Footer;