# Weather-cli
A dead-simple, super wimpy cli weather tool.

## Setup

1. Go to https://openweathermap.org/price, sign up for the free tier and get an api key.
2. Clone the repo
```bash
git clone <repo>

poetry init
poetry build
```

3. Navigate to where you'd like to install the package
```bash
poetry init
poetry add wheel
poetry add <path/to/dist/weather_cli-0.1.0-py3-none-any.whl>

OR 

pip install <path/to/dist/weather_cli-0.1.0-py3-none-any.whl>
```

4. Export your credentials 
```bash
export API_KEY=<YOUR_API_KEY_FROM_STEP_1>
```

5. Use it 
```bash
╰─ weather_cli london
London, GB [Lat: 51.5085, Lon:-0.1257]

Feels like 37°, Clouds.

Low: 41°
High: 46°
Humidity: 80%

https://openweathermap.org/city/2643743
```
