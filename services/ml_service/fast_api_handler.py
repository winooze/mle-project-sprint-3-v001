"""Класс FastApiHandler, который обрабатывает запросы API."""
from catboost import CatBoostRegressor

class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # типы параметров запроса для проверки
        self.param_types = {
            "id": str,
            "model_params": dict
        }

        self.model_path = "/home/mle-user/mle-projects/mle-project-sprint-3-v001/services/models/estate_best_model.cbm"
        self.load_model(model_path=self.model_path)
        
        # необходимые параметры для предсказаний модели оттока
        self.required_model_params = [
            'is_apartment',
            'studio',
            'has_elevator',
            'building_type_int',
            'floor',
            'kitchen_area',
            'living_area',
            'rooms',
            'total_area',
            'build_year',
            'latitude',
            'longitude',
            'ceiling_height',
            'flats_count',
            'floors_total'
        ]


    def load_model(self, model_path: str):
        """Загружаем обученную модель.
        Args:
            model_path (str): Путь до модели.
        """
        try:
            self.model = CatBoostRegressor()
            self.model.load_model(model_path)
        except Exception as e:
            print(f"Failed to load model: {e}")

    def price_predict(self, model_params: dict) -> float:
        """Предсказываем цену недвижимости.
        Args:
            model_params (dict): Параметры для модели.
        Returns:
            target - стоимость объекта в млн. руб. 
    """
        param_values_list = list(model_params.values())
        return round(self.model.predict(param_values_list), 2) 
        
    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора параметров.
        
        Args:
            query_params (dict): Параметры запроса.
        Returns:
            bool: True - если есть нужные параметры, False - иначе
        """
        if "id" not in query_params or "model_params" not in query_params:
            return False 
        if not isinstance(query_params['id'], self.param_types['id']):
            return False 
        if not isinstance(query_params['model_params'], self.param_types['model_params']): 
            return False
        return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверяем параметры пользователя на наличие обязательного набора.
        
        Args:
        model_params (dict): Параметры пользователя для предсказания.
        
        Returns:
        bool: True - если есть нужные параметры, False - иначе
        """
        if set(model_params.keys()) == set(self.required_model_params): 
            return True
        return False 
    
    def validate_params(self, params: dict) -> bool:
        """Разбираем запрос и проверяем его корректность.
        
        Args:
        params (dict): Словарь параметров запроса.
        
        Returns:
        - **dict**: Cловарь со всеми параметрами запроса.
        """
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
        
        if self.check_required_model_params(params["model_params"]):
            print("All model params exist")
        else:
            print("Not all model params exist")
            return False
        return True
        
    def handle(self, params):
        """Функция для обработки запросов API параметров входящего запроса.

        Args:
            params (dict): Словарь параметров запроса.

        Returns:
            dict: Словарь, содержащий результат выполнения запроса.
        """
        try:
            if not self.validate_params(params):
                response = {'Error': 'Problem with parameters'}
            else: 
                id = params["id"]
                model_params = params["model_params"]
                print(f"Predicting for id: {id} and model_params:\n{model_params}")
                pred_price = self.price_predict(model_params=model_params)
                response = {
                    "id": id, 
                    "prediction": pred_price
                }

        except Exception as e:
            print(f"Error while handling request: {e}")
        else:
            return response
        

if __name__ == "__main__":
    # создаём тестовый запрос
    test_params = {
        "id": "123",
            "model_params": {
                'is_apartment': False,
                'studio': False,
                'has_elevator': True,
                'building_type_int': 4,
                'floor': 5,
                'kitchen_area': 0.0,
                'living_area': 0.0,
                'rooms': 2,
                'total_area': 52.0,
                'build_year': 2007,
                'latitude': 55.72347640991211,
                'longitude': 37.903202056884766,
                'ceiling_height': 2.740000009536743,
                'flats_count': 376,
                'floors_total': 11
            }
    }

    # создаём обработчик запросов для API
    handler = FastApiHandler()

    # делаем тестовый запрос
    response = handler.handle(test_params)
    print(f"Response: {response}")