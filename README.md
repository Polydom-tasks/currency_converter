# Currency Converter

## Endpoints
| Method | Endpoint      | Description                                                    | Example                                         |
|--------|---------------|----------------------------------------------------------------|-------------------------------------------------|
| GET    | /currencies   | Retrieves a list of all supported currencies                   | `GET /currencies`                               |
| GET    | /last_update  | Retrieves the timestamp of the last update                     | `GET /last_update`                              |
| GET    | /convert      | Converts an amount from one currency to another                | `GET /convert?source=USD&target=EUR&amount=100` |
| POST   | /update_rates | Updates the exchange rates using the external currency service | `POST /update_rates`                            |

## Launch
Use Docker Compose to launch the project:
```
docker-compose up --build
```
The database will initialize with data right after the command, no additional actions required.         
