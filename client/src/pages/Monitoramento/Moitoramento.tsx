import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

function Monitoramento() {
    return (
        <div>
            <Header />
            <main className="flex flex-col justify-start items-center py-0 px-[1.25rem] text-left bg-white my-[1.25rem]">
                <div>
                    <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Monitoramento</h1>
                    <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
                    O monitoramento dos gastos públicos foi realizado por meio da análise da API do Querido Diário. 
                    Essa ferramenta foi fundamental para obter informações detalhadas sobre os contratos e transações no setor público, 
                    permitindo identificar padrões importantes nos dados. Com uma observação cuidadosa, foi possível organizar as informações de forma mais clara e estruturada.
                    </p>
                    <p className="text-[1.2rem] leading-[1.6] mb-[1.5rem] max-w-[50rem] w-full">
                    Aqui estão os principais pontos-chave utilizados para o monitoramento:
                    </p>
                </div>
                <div className="w-full max-w-4xl text-center">
                    <ul className="list-disc text-lg leading-7 text-left  mx-auto mb-4 w-auto">
                        <li className="mb-3 text-black">
                            <strong>Nome do Fornecedor:</strong> A API forneceu acesso aos nomes dos fornecedores envolvidos nas transações, 
                            o que foi fundamental para entender quem eram as empresas responsáveis pelos serviços ou produtos adquiridos.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Data de Assinatura e Publicação:</strong> As datas de assinatura e publicação dos contratos foram analisadas 
                            para garantir que tudo estivesse sendo feito dentro dos prazos estabelecidos pela lei, o que também reforça a transparência nesse processo.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Vigência:</strong> Também foi dada atenção à vigência dos contratos, para verificar os períodos de validade e execução dos serviços ou fornecimentos, 
                            ajudando a manter o controle sobre o que estava sendo acordado.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>CNPJ:</strong> O CNPJ dos fornecedores foi um dado chave para assegurar que as empresas envolvidas nas transações estavam devidamente registradas, 
                            o que garante a legalidade de todo o processo.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Valores:</strong> A análise dos valores foi crucial para entender o quanto estava sendo gasto em cada transação. Isso permitiu comparar diferentes contratos 
                            e identificar possíveis inconsistências ou áreas que precisavam de mais atenção.
                        </li>
                    </ul>
                </div>
            </main>
            <Footer />
        </div>
    );
}

export default Monitoramento;
