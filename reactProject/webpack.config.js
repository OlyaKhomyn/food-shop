const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

const outputPath = path.join(__dirname, 'dist');
const srcPath = path.resolve(__dirname, 'src');

module.exports = {
  entry: ['babel-polyfill', path.join(srcPath, 'index.js')],
  output: {
    path: outputPath,
    filename: 'bundle.js'
  },
  target: 'web',
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.css$/,
        use: [
          'style-loader',
          {
            loader: require.resolve('css-loader')
          }
        ]
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg|img|jpg)$/,
        loader: 'url-loader?limit=100000'
      }
    ]
  },
  resolve: {
    alias: {
      src: srcPath
    },
    extensions: ['*', '.js', '.jsx']
  },
  devServer: {
    port: 3000,
    historyApiFallback: true
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',
      favicon: './public/favicon.png'
    })
  ]
}
