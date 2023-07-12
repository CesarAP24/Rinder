const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  // ...otras configuraciones de Vue CLI

  // Configuración de Webpack
  configureWebpack: {
    module: {
      rules: [
        // ...otras reglas de Webpack

        // Agrega esta regla para manejar archivos PNG
        {
          test: /\.(png|jpe?g|gif)$/i,
          use: [
            {
              loader: "file-loader",
              options: {
                name: "[name].[ext]",
                outputPath: "images/",
              },
            },
          ],
        },
      ],
    },
  },
});
