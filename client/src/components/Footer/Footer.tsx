import React from 'react';
import './Footer.css';

function Footer() {
return (
  <footer className="App-footer">
    <div className="linha"></div>
    <div className="logo-container">
        <img src="/assets/logo.png" className="App-logo" alt="logo" />
        <div id="title_footer">Gastos Públicos</div>
    </div>
    <ul className="navigation__footer">
        <li><a className="navigation__footerLink" href="" target="_blank" rel="noopener noreferrer">Gastos</a></li>
        <li><a className="navigation__footerLink" href="" target="_blank" rel="noopener noreferrer">Monitoramento</a></li>
        <li><a className="navigation__footerLink" href="/SobreProjeto" target="_blank" rel="noopener noreferrer">Sobre o projeto</a></li>
        <li><a className="navigation__footerLink" href="/SobreNos" target="_blank" rel="noopener noreferrer">Sobre nós</a></li>
      </ul>
    <div>
      <img src="/assets/logoUnb.png" className="Unb-logo" alt="Logo UnB" />
    </div>
  </footer>
);
}

export default Footer;