# Usa uma imagem oficial do Node.js como base
FROM node:18-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY package.json package-lock.json ./

# Instala as dependências
RUN npm install

# Copia o restante do código do projeto
COPY . .

# Expõe a porta padrão do React
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["npm", "start"]
