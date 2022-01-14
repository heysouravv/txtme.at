from typing import Optional
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return '''
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>TXTME.AT</title>
                <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet" />
            </head>
            <body>
                <div class='flex items-center justify-center min-h-screen from-gray-100 via-gray-300 to-gay-500 bg-gradient-to-br'>
                    <div class="relative w-full h-screen">
                    <div class="absolute-center">
                        <svg class="circle-svg" viewBox="0 0 500 500">
                            <defs>
                                <path d="M50,250c0-110.5,89.5-200,200-200s200,89.5,200,200s-89.5,200-200,200S50,360.5,50,250"
                                    id="textcircle_top">
                                    <animateTransform attributeName="transform" begin="0s" dur="20s" type="rotate" from="0 250 250"
                                        to="360 250 250" repeatCount="indefinite" />
                                </path>
                            </defs>
                            <text class="circle-text" dy="70" textLength="1220">
                                <textPath xlink:href="#textcircle_top">
                                    WE MADE YOUR SHARING SIMPLE
                                </textPath>
                            </text>
                        </svg>
                
                    </div>
                <style>
                            .showreels-btn {
                            width: 25%;
                            height: 25%;
                            display: block;
                            margin: 0;
                            position: absolute;
                            top: 50%;
                            left: 55%;
                            -ms-transform: translate(-55%, -50%);
                            transform: translate(-55%, -50%);
                        }
                
                        .showreels-div:hover .showreels-video {
                            display: block;
                        }
                
                        .showreels-div:hover .showreels-btn {
                            display: none;
                        }
                
                            .circle-text {
                            font-size: 24px;
                            font-weight: 700;
                            text-transform: uppercase;
                            letter-spacing: 10px;
                            fill: #333;
                        }
                
                        .showreels-div {
                            height: 150px;
                            width: 150px;
                            border-radius: 100%;
                        }
                
                        .showreels-video {
                            border-radius: 100%;
                            width: 100%;
                            height: 100%;
                            object-fit: cover;
                            display: none;
                        }
                
                            .circle-svg {
                            height: 350px;
                            width: 350px;
                        }
                        .absolute-center {
                            margin: 0;
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                        }
                
                </style>
            </body>
        </html> '''

@app.get("/{w}", response_class=RedirectResponse)
async def redirect_fastapi(w: str):
    return "https://wa.me/{0}?text=Hi".format(w)
