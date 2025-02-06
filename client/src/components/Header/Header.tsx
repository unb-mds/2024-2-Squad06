import React, { useState } from 'react';

function Header() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="bg-white">
      <img src="/assets/unb.png" className="mx-auto max-w-28" alt="Unb" />
      <header className="flex flex-col 1125:flex-row 1125:justify-center 1125:space-x-[5rem] 1125:items-center bg-blue-600 text-white 1125:gap-[6.5rem] px-4 py-2 1125:text-center">
        <div className="flex flex-row space-x-[5rem] items-center justify-center w-full 1125:w-auto 1125:space-x-[0rem]">
          <div className="flex flex-row items-center">
            <img src="/assets/logo.png" className="h-28 w-28" alt="Logo do App" />
            <div id="title" className="ml-2 1125:ml-0 text-4xl font-bold">
              <a href="/" className="text-white hover:underline no-underline">Gastos Públicos</a>
            </div>
          </div>

          <button
            className="1125:hidden text-6xl p-2 text-white focus:outline-none "
            onClick={toggleSidebar}
          >
            ☰
          </button>
        </div>

        <nav
          className={`fixed inset-0 bg-blue-600 transform ${
            isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
          } transition-transform duration-300 1125:relative 1125:transform-none 1125:flex 1125:items-center`}
          style={{ zIndex: 20 }}
        >
          <ul className="flex flex-col 1125:flex-row 1125:items-center items-center justify-center space-y-8 1125:space-y-0 1125:space-x-6 p-4 1125:p-0 1125:pb-0 1125:m-0">
            <li>
              <a
                className="text-white font-bold text-sm uppercase hover:underline no-underline"
                href="/Gastos"
              >
                Gastos
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase hover:underline no-underline"
                href="/Monitoramento"
              >
                Monitoramento
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase hover:underline no-underline"
                href="/SobreProjeto"
              >
                Sobre o projeto
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase hover:underline no-underline"
                href="/SobreNos"
              >
                Sobre nós
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase hover:underline no-underline"
                href="/Filtragem"
              >
                Área de Busca
              </a>
            </li>
          </ul>
          <button
            className="absolute top-4 left-4 text-white text-2xl 1125:hidden"
            onClick={toggleSidebar}
          >
            ✕
          </button>
        </nav>
      </header>
    </div>
  );
}

export default Header;