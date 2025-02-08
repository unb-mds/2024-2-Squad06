import React from 'react';
function Footer() {
  return (
    <footer className="flex flex-col justify-center items-center bg-[#112632] text-white text-center p-[1.25rem_0] relative bottom-0 w-full pt-[2rem] 860:flex-row 860:gap-[6.5rem]">
      <div className="w-full border-b-[0.1875rem] border-white absolute top-[1.25rem] z-10"></div>
      <div className="flex justify-center items-center mb-0">
          <img src="/assets/logo.png" className=" mb-0 max-w-[5.625rem]" alt="logo" />
          <div id="title" className="ml-2 1125:ml-0 text-3xl font-bold">
                Gastos Públicos
            </div>
      </div>
      <ul className="flex flex-col items-center gap-[1rem] list-none text-white p-0 m-0 860:flex-row 860:gap-[2rem]">
          <li><a className="text-white no-underline hover:underline " href="/" target="_blank" rel="noopener noreferrer">Home</a></li>
          <li><a className="text-white no-underline hover:underline" href="/Filtragem" target="_blank" rel="noopener noreferrer">Área de Busca</a></li>
          <li><a className="text-white no-underline hover:underline" href="/SobreProjeto" target="_blank" rel="noopener noreferrer">Sobre o projeto</a></li>
          <li><a className="text-white no-underline hover:underline" href="/SobreNos" target="_blank" rel="noopener noreferrer">Sobre nós</a></li>
        </ul>
      <div>
        <img src="/assets/logoUnb.png" className="max-w-[5rem] self-center pt-[1.0rem] 860:max-w-[5.625rem] 860:pt-0" alt="Logo UnB" />
      </div>
    </footer>
  );
 }
  
  export default Footer;