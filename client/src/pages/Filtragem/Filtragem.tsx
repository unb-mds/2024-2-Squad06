import React, { useState } from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/home/BarraPesquisa/BarraPesquisa';
import BarraFiltragem from '../../components/home/BarraFiltragem/BarraFiltragem';
import CardGasto from '../../components/CardGastos/CardGastos';

function Filtragem() {
    return (
        <div>
            <Header />
            <div className="mt-5">
                <BarraPesquisa />
            </div>
            <div className="sm:mt-5 mt-0 ml-2 flex flex-col md:flex-row md:justify-center">
                <div className="md:h-screen mt-0 flex flex-col items-center justify-start p-4">
                    <BarraFiltragem />
                </div>
                
                <div className="flex flex-col gap-4 items-center justify-center ">
                    <CardGasto className=" mt-5 transition-all duration-700 max-w-[90%] md:max-w-[75%]" />
                    <CardGasto className=" mt-0 transition-all duration-700 max-w-[90%] md:max-w-[75%]" />
                    <CardGasto className=" mt-0 transition-all duration-700 max-w-[90%] md:max-w-[75%]" />
                </div>
            </div>
            <Footer />
        </div>
    );
}

export default Filtragem;
