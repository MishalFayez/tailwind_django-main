/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../tailwindapp/**/*.{html,js}"],
  theme: {
    extend: {

      animation :{

        slowping:'slowping 1s cubic-bezier(0, 0, 0.2, 1) infinite',

        fastpulse:'fastpulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',

      },

      keyframes:{

      slowping: {

        '95%, 100%': {transform: 'scale(1.15)', opacity:'0'},

        '15%': {transform:'rotate(360deg)'}

      },

      fastpulse: {

      //   50% {

      //     opacity: .5;

      // }

      '50%': {opacity: '0.5'},

      '15%': {transform:'scale(2)'}

      }

    },

      screens: {

        'xs': '480px',

      },

    },
  },
  plugins: [],
}
