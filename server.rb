require 'sinatra'
require 'json'

post '/payload' do
  payload = JSON.parse(params[:payload])
  "Well it worked!"
end

get '/payload' do
  "Try a post request"
end
