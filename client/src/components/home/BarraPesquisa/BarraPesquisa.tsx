import React from 'react';

function BarraPesquisa() {
  return (
    <div className="flex flex-row justify-center items-center my-4 1300:max-w-[100rem] 1300:mx-auto 1300:my-5">
        <img className="hidden 580:block 580:w-[1.5rem] 580:h-[1.5rem] 580:mr-[1rem] " src="/assets/lupa.png" alt="Lupa" />
        <form action="/" method="GET">
          <input
            type="text"
            className="w-[60vw] py-[0.625rem] text-base border-b-[0.125rem] border-[#363636] bg-transparent outline-none mr-5 1300:w-[48.875rem]"
            placeholder="Pesquise por um gasto"
            required
          />
          <input
            type="submit"
            className="bg-[#116FBB] text-white border-none rounded-[1.5625rem] py-[0.75vw] px-[4vw] text-base cursor-pointer h-[2.5rem] transition-colors duration-500 hover:bg-[#112632] 1300:px-[2.5rem] 1300:py-[0.5rem]"
            value="Buscar"
          />
        </form>
        <a href="/Filtragem">
          <img className="w-[2.1rem] h-[2.1rem] ml-4" src="/assets/filtro.png" alt="Filtrar" />
        </a>
      </div>
  );
}

export default BarraPesquisa;