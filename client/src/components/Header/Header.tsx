import React, { useState } from 'react';

function Header() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="bg-white">
      <img src="/assets/unb.png" className="mx-auto max-w-28" alt="Unb" />
      <header className="flex flex-col lg:flex-row lg:justify-between lg:items-center bg-blue-600 text-white px-4 py-2">
        <div className="flex flex-row items-center justify-between w-full lg:w-auto">
          <div className="flex flex-row items-center">
            <img src="/assets/logo.png" className="h-28 w-28 lg:ml-4" alt="Logo do App" />
            <div id="title" className="ml-2 lg:ml-4 text-xl lg:text-4xl font-bold">
              <a href="/" className="text-white hover:text-gray-300 no-underline">Gastos Públicos</a>
            </div>
          </div>

          <button
            className="lg:hidden text-2xl p-2 text-white focus:outline-none"
            onClick={toggleSidebar}
          >
            ☰
          </button>
        </div>

        <nav
          className={`fixed inset-0 bg-blue-600 transform ${
            isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
          } transition-transform duration-300 lg:relative lg:transform-none lg:flex lg:items-center`}
          style={{ zIndex: 50 }}
        >
          <ul className="flex flex-col lg:flex-row items-center justify-center space-y-6 lg:space-y-0 lg:space-x-8 p-4 lg:p-0">
            <li>
              <a
                className="text-white font-bold text-sm uppercase tracking-wider hover:underline no-underline"
                href="/Gastos"
              >
                Gastos
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase tracking-wider hover:underline no-underline"
                href="/Monitoramento"
              >
                Monitoramento
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase tracking-wider hover:underline no-underline"
                href="/SobreProjeto"
              >
                Sobre o projeto
              </a>
            </li>
            <li>
              <a
                className="text-white font-bold text-sm uppercase tracking-wider hover:underline no-underline"
                href="/SobreNos"
              >
                Sobre nós
              </a>
            </li>
          </ul>
          <button
            className="absolute top-4 left-4 text-white text-2xl lg:hidden"
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
