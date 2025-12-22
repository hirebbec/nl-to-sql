from langchain_core.tools import tool

@tool
def get_db_ddl() -> str:
    """
    Возвращает DDL базы данных с таблицами ДТП
    """
    return """
           create table public.accidents
           (
               accident_number varchar not null primary key unique,
               accident_datetime  timestamp with time zone not null,
               category accidentcategories not null,
               district_name districtnames not null references public.districts,
               place varchar,
               street varchar,
               house varchar,
               road varchar,
               federal_highway federalhighways,
               kilometer integer,
               meter integer,
               died integer not null,
               wounded integer not null,
               children_died integer,
               children_wounded integer,
               road_operation_flaws character varying[],
               road_arrangement_flaws character varying[],
               road_conditions_flaws character varying[],
               objects_on_site character varying[],
               objects_nearby character varying[],
               traffic_factors character varying[],
               road_condition varchar,
               weather_conditions character varying[],
               light_condition varchar,
               road_plane varchar,
               road_profile varchar,
               lane_count integer,
               accident_occurred_lane integer,
               road_width integer,
               roadside_width integer,
               sidewalk_width integer,
               dividing_strip_width integer,
               dividing_strip_type varchar,
               road_surface_type varchar,
               street_category varchar,
               road_category varchar,
               road_value varchar,
               participants_count integer,
               cars_count integer,
               driving_changes varchar,
               accident_scheme_url varchar,
               created_at timestamp with time zone not null,
               updated_at timestamp with time zone,
               latitude double,
               longitude double,
               season varchar not null, 
               month varchar not null,
               weekday varchar not null,
               day_type daytypesenum NOT NULL
           );

           create table public.cars
           (
               car_number varchar not null primary key unique,
               car_location_leaving varchar not null,
               car_type varchar,
               brand varchar,
               model varchar,
               color varchar,
               car_damage_places varchar,
               technical_malfunctions varchar,
               vehicle_specs varchar,
               model_year integer,
               ownership_form varchar,
               accident_number varchar not null references public.accidents,
               created_at timestamp with time zone not null,
               updated_at timestamp with time zone
           );

           create table public.participants
           (
               participant_number varchar not null primary key unique,
               participant_category varchar,
               gender varchar,
               driving_experience integer,
               drunkenness_level integer,
               participant_location_leaving varchar,
               severity_level varchar,
               direct_violations character varying[],
               related_violations character varying[],
               seatbelt_used varchar,
               child_restraint_type varchar,
               car_number varchar not null references public.cars,
               created_at timestamp with time zone not null,
               updated_at timestamp with time zone
           ); 
            Отныне маркируй каждую часть ответа специальными тегами:
            <|text|> — начало текстового блока
            <|sql|> — начало SQL-кода
            Если в ответе несколько блоков одного типа (например, несколько текстовых частей), каждый из них должен начинаться с нового тега.
            Пример структуры:
            <|text|>Пояснение к задаче.
            <|sql|>
            SELECT * FROM users;
            <|text|>Описание результата.
            Всегда используй эти теги при генерации ответов."""
