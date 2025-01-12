/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      screens: {
        '860': '860px',
        '1008':'1008px',
        '1300':'1300px',
      },
    },
  },
  plugins: [],
};