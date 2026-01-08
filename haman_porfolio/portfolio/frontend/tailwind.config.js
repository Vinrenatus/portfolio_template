/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#FF6B35', // Vibrant orange-red
        secondary: '#F7931E', // Vibrant orange
        accent: '#FFD23F', // Vibrant yellow
        dark: '#2D3748', // Dark blue-gray
        light: '#F7FAFC', // Light blue-white
      }
    },
  },
  plugins: [],
}

