// import React, {Component} from 'react';
// import ReactDOM from 'react-dom';

class RentForm extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            customers: [],
            products: [],
            rentDetails: [
                { index: 0, product: 1, count: 99 },
                { index: 1, product: 1, count: 55 },
            ],
        }

        this.handleRentDetailDelete = (index) => {

        }

        this.handleRentDetailChange = (rentDetail) => {
            const s = [
                ...this.state.rentDetails.slice(0, rentDetail.index),
                rentDetail,
                ...this.state.rentDetails.slice(rentDetail.index + 1)
            ];
            console.log(s);
            this.setState({
                rentDetails: [
                    ...this.state.rentDetails.slice(0, rentDetail.index),
                    rentDetail,
                    ...this.state.rentDetails.slice(rentDetail.index + 1)
                ]
            });
        }

        this.handleAdd = (event) => {
            event.preventDefault();
            this.setState({ rentDetails: [...this.state.rentDetails, { index: 2 }] });
        }
    }

    componentDidMount() {
        $.get('http://127.0.0.1:8000/api/customers/?format=json', (customers) => {
            this.setState({ customers });
        });
        $.get('http://127.0.0.1:8000/api/products/?format=json', (products) => {
            this.setState({ products });
        });
    }

    render() {
        const numbers = [0, 1, 2];

        const customerOptions = this.state.customers.map(customer =>
            <option value={customer.id}>{customer.name}</option>
        )
        const rentDetailItems = this.state.rentDetails.map((item) =>
            <RentDetailForm
                products={this.state.products}
                onRentDetailDelete={this.handleRentDetailDelete}
                onChange={this.handleRentDetailChange}
                rentDetail={item} />
        )

        return (
            <div>
                <div>
                    <label>
                        customer:
                        <select name="customer">
                            <option value selected>----</option>
                            {customerOptions}
                        </select>
                    </label>
                    <br />
                    <label>
                        happen_date:
                        <input name="happen_date" type="text" />
                    </label>
                    <br />
                </div>
                {rentDetailItems}

                <button onClick={this.handleAdd}>Add</button>
            </div>

        );
    }
}

class RentDetailForm extends React.Component {
    constructor(props) {
        super(props);

        this.handleDelete = (event) => {
            this.props.onRentDetailDelete(this.props.index);
            event.preventDefault();
        }

        this.handleChange = (event) => {
            const target = event.target;
            console.log(target.name, target.value);
            var copy = Object.assign({}, this.props.rentDetail, { [target.name]: target.value });
            this.props.onChange(copy);
        }
    }

    render() {
        const { products, rentDetail } = this.props;
        const productOptions = products.map(product =>
            <option value={product.id}>{product.name}</option>
        );
        return (
            <div>
                <label>
                    product:
                    <select
                        name="product"
                        value={rentDetail.product}
                        onChange={this.handleChange}
                    >
                        <option value="-1">----</option>
                        {productOptions}
                    </select>
                </label>

                <label>
                    count:
                    <input
                        name="count"
                        type="text"
                        value={rentDetail.count}
                        onChange={this.handleChange}
                    />
                </label>
                <button onClick={this.handleDelete}>Delete</button>
            </div>
        )
    }
}

ReactDOM.render(<RentForm />, document.getElementById('root'));