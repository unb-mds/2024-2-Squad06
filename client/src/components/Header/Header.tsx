import React, { useState } from 'react';
import './Header.css';

function Header() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="bg-white">
      <img src="/assets/unb.png" className="unb mx-auto" alt="Unb" />
      <header className="flex justify-between items-center p-3 bg-blue-600 text-white">
        <div className="logo-container flex items-center">
          <img src="/assets/logo.png" className="App-logo " alt="Logo do App" />
          <div id="title" className="ml-3 text-xl">
            <a href="/" className="text-white hover:text-gray-300">Gastos Públicos</a>
          </div>
        </div>

        <button className="lg:hidden p-2 text-white sidebar-toggle" onClick={toggleSidebar}>
          ☰
        </button>

        <nav
          className={`inset-0 bg-gray-800 bg-opacity-100 z-50 transform 
          ${isSidebarOpen ? 'translate-x-0 w-48' : '-translate-x-full w-48'} 
          transition-transform duration-300 lg:relative lg:flex lg:items-center lg:justify-center lg:bg-transparent`}
        >
          <ul className="flex flex-col text-xl lg:flex-row items-center justify-center space-y-5 lg:space-y-0 lg:space-x-6 w-auto">
            <li><a className="text-white hover:text-gray-300 navigation__link whitespace-nowrap" href="/Gastos">Gastos</a></li>
            <li><a className="text-white hover:text-gray-300 navigation__link whitespace-nowrap" href="/Monitoramento">Monitoramento</a></li>
            <li><a className="text-white hover:text-gray-300 navigation__link whitespace-nowrap" href="/SobreProjeto">Sobre o projeto</a></li>
            <li><a className="text-white hover:text-gray-300 navigation__link whitespace-nowrap" href="/SobreNos">Sobre nós</a></li>
          </ul>

          <button 
            className="absolute left-0 text-white p-2 lg:hidden text-2xl"
            onClick={toggleSidebar}
          >
            ☰
          </button>
        </nav>
      </header>
    </div>
  );
}

export default Header;
