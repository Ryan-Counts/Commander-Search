export default class APIService {
    static search(colors, searchTerms) {
        return fetch('/api/search', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ colors, searchTerms }),
        })
            .then(async (response) => {
                const data = await response.json().catch(() => null);

                if (response.status === 404) {
                    throw new Error('No cards matched that search. Try removing or changing a criterion.');
                }
                if (!response.ok || !data || data.object === 'error') {
                    throw new Error('Something went wrong with the search. Please try again.');
                }
                return data;
            })
            .catch((err) => {
                // fetch itself failed (offline, server down)
                if (err instanceof TypeError) {
                    throw new Error("Couldn't reach the server. Check your connection and try again.");
                }
                throw err;
            });
    }
}