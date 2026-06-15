"""ShopTalk API package.

This package provides the FastAPI application and route definitions
for the ShopTalk sales desk API.

Modules
-------
main
    FastAPI application entry point with health check and app configuration.
routes
    Route handlers for all ShopTalk API endpoints.

Usage
-----
Start the development server::

    uvicorn shoptalk.api.main:app --reload

Or import the app directly::

    from shoptalk.api.main import app
"""
