import React from 'react';
import './Header.css';

function Header() {
  return (
    <div>
      <img src="/assets/unb.png" className="unb" alt="Unb" />
      <header className="App-header">
        <div className="logo-container">
          <img src="/assets/logo.png" className="App-logo" alt="Logo do App" />
          <div id="title">
            <a href="/">Gastos Públicos</a>
          </div>
        </div>
        <ul className="navigation">
          <li><a className="navigation__link" href="/Gastos" target="_blank" rel="noopener noreferrer">Gastos</a></li>
          <li><a className="navigation__link" href="" target="_blank" rel="noopener noreferrer">Monitoramento</a></li>
          <li><a className="navigation__link" href="/SobreProjeto" target="_blank" rel="noopener noreferrer">Sobre o projeto</a></li>
          <li><a className="navigation__link" href="/SobreNos" target="_blank" rel="noopener noreferrer">Sobre nós</a></li>
        </ul>
      </header>
    </div>
  );
}

export default Header;