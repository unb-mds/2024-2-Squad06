import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';

function Gastos() {
    return (
        <div>
            <Header />
            <main className="flex flex-col justify-start items-center py-0 px-[1.25rem] text-left bg-white my-[1.25rem]">
                <div>
                    <h1 className="text-[2.5rem] mb-[1.25rem] text-center">O que são Gastos públicos?</h1>
                    <p className="text-[1.2rem] leading-[1.6] mb-[0.9375rem] max-w-[55rem] w-full">
                        Gastos públicos referem-se ao dinheiro que o governo utiliza para financiar as suas atividades, como a prestação de serviços públicos (saúde, educação, segurança), infraestrutura, investimentos em projetos sociais e o pagamento de dívidas. 
                        Esses gastos são realizados com recursos obtidos por meio da arrecadação de impostos, taxas e contribuições, e são essenciais para garantir o funcionamento do Estado e o bem-estar da sociedade.
                    </p>
                    <p className="text-[1.2rem] leading-[1.6] mb-[1.5rem] max-w-[50rem] w-full">
                    Além disso, a gestão eficiente dos gastos públicos é crucial para o desenvolvimento econômico e social, 
                    garantindo que os recursos sejam alocados de forma responsável e que as políticas públicas atendam às necessidades da população de maneira justa e eficaz. O controle e a transparência nos gastos públicos são fundamentais para evitar desperdícios, 
                    combater a corrupção e assegurar que os recursos sejam utilizados de acordo com o interesse público.
                    </p>
                </div>
                <div className="w-full max-w-4xl text-center">
                    <h1 className="text-[2.5rem] mb-[1.25rem] text-center">Pontos Importantes</h1>
                    <ul className="list-disc text-lg leading-7 text-left  mx-auto mb-4 w-auto">
                        <li className="mb-3 text-black">
                            <strong>Transparência:</strong> A população deve exigir clareza na gestão dos recursos públicos para garantir eficiência e evitar desperdícios.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Impostos:</strong> Os impostos pagos pela sociedade financiam os serviços públicos, por isso, é importante entender como o governo utiliza esse dinheiro.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Orçamento e Prioridades:</strong> O governo define suas prioridades no orçamento, e é essencial que a população compreenda onde o dinheiro será investido.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Dívidas públicas:</strong> Parte dos gastos é destinada ao pagamento de dívidas, o que pode impactar outras áreas e políticas fiscais.
                        </li>
                        <li className="mb-3 text-black">
                            <strong>Participação cidadã:</strong> A população pode influenciar nas decisões sobre o uso dos recursos públicos, garantindo um uso responsável e eficaz do dinheiro arrecadado.
                        </li>
                    </ul>
                </div>
            </main>
            <Footer />
        </div>
    );
}

export default Gastos;
